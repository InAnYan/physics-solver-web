from django.shortcuts import render
from physics_solver.exceptions import SolverError, ParseError
from physics_solver.problem_parser import parse_english_problem
from physics_solver.string_solution import StringSolution
from spacy import displacy


def index(request):
    return render(request, 'index.html')


def solution(request):
    text = request.GET.get('text')
    context = {'problem_text': text}

    try:
        (problem, doc) = parse_english_problem(text)
        solution = problem.solve()
        context['solution'] = StringSolution(problem, solution)
        context['displacy_ents'] = displacy.render(doc, style='ent')
    except ParseError | SolverError:
        pass

    return render(request, 'solution.html', context)
