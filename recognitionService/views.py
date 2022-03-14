from .ML_Model.mlpredict import mlpredict
from .DL_Model.dlpredict import dlpredict
from .forms import DialectRecognizerForm

from django.shortcuts import render

# Create your views here.

# def DialectRecognizerLanding(request):
def landingPage(request):
    return render(request, 'recognitionService/landing.html')


def DialectRecognizer(request, model):

    context = {
        'model': model,
        'form': DialectRecognizerForm(),
        'valid_POST': False,
    }

    prediction = 'false'
    if request.method == 'POST':
        form = DialectRecognizerForm(request.POST)

        if form.is_valid():
            context['valid_POST'] = True
            print('valid!-',end='')
            text = form.cleaned_data['text']
            # print('valid@-',end='')
            # print('valid#-',end='')
            # print('valid$-',end='')
            # print('valid%-',end='')

            try:
                if model == 'ml':
                    prediction = mlpredict(text)
                elif model == 'dl':
                    prediction = dlpredict(text)
                else:
                    prediction = None
                context['predicted_dialect'] = prediction
                print(context['predicted_dialect'])
            except Exception as e:
                print(e)
        else:
            print('notvalid')

    return render(request, 'recognitionService/result/model.html', context)


# def DialectRecognizerML(request):
#     return DialectRecognizer(request, 'mlmodel')


# def DialectRecognizerDL(request):
#     return DialectRecognizer(request, 'dlmodel')
