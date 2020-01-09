from django.shortcuts import render, redirect

from .models import Problem
from submission.models import Submission
from .forms import SubmitForm
from Judge_dir.judge import judging

#To view all problems
def problem_list(request):
    problems = Problem.objects.all().order_by('id')
    context = {'problems' : problems}    
    return render(request, 'problems.html', context)

def problem_id(request, pid):
    if request.method == 'POST':
        form = SubmitForm(request.POST, request.FILES)  
        if form.is_valid():
            code = form.save(commit = False) #variable name need to change
            code.user_id = request.user
            problem = Problem.objects.get(id=pid)
            problem.no_of_submissions += 1
            code.problem_id = problem
            code.save() #save the model before judging with default values
			#need to redirect to current submission page (not implemented)
            
            if code.language == 'Python': #Time limit for different language
                time = problem.time_limit[1]
            else:
                time = problem.time_limit[0]
            
            code.verdict, code.time = judging(problem.input_file.path, problem.output_file.path, code.code.path, code.language, time, problem.memory_limit)
            
            if code.verdict == 1:
                problem.no_of_accepted += 1
			#final save after judging
            code.save()
            problem.save()
            return redirect('submit')
    else:
        form = SubmitForm()
        problem = Problem.objects.get(id = pid)
        request.session['pid'] = pid
        context = {'problem' : problem, 'form' : form}
        return render(request, 'problem.html', context)

#To view all submissions, function name need to change
def submit_code(request):
    submission = Submission.objects.all().order_by('-id') #descending order
    context = {'submission' : submission}
    return render(request, 'submit.html', context)
