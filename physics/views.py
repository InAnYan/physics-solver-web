from datetime import datetime

from django.shortcuts import render
from physics_solver.parser.nlp import patterns
from physics_solver.parser.problem_parser import *
from physics_solver.util.exceptions import SolverError
from spacy import displacy

from physics.models import ImprovementReport, ProblemIssueReport


def index(request):
    return render(request, 'index.html')


def solution(request):
    text = request.GET.get('text')

    context = {'problem_text': text}

    doc = recognize_entities(text)
    context['displacy_ents'] = displacy.render(doc, style='ent', options={'colors': patterns.generate_colors()})

    try:
        problem = parse_english_document(doc)
        context['solution'] = problem.solve_and_make_string_solution()
    except ParseError as e:
        context['parse_error'] = e.msg
    except SolverError as e:
        context['solver_error'] = e.msg

    return render(request, 'solution.html', context)


def thanks_feedback(request):
    report = ImprovementReport(author_name=request.POST.get('author_name'),
                               author_email=request.POST.get('author_email'),
                               text=request.POST.get('text'),
                               date=datetime.now())
    report.save()

    return render(request, 'thanks-feedback.html')


def thanks_report(request):
    problem_text = request.POST.get('text')
    if not problem_text:
        problem_text = ''

    report = ProblemIssueReport(is_solved=request.POST.get('action') == 'incorrect',
                                problem_text=problem_text,
                                comment=request.POST.get('comment'),
                                date=datetime.now())
    report.save()

    return render(request, 'thanks-report.html')


def no_link(request):
    return render(request, 'no-link.html')
