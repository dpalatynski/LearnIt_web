from django.shortcuts import render
from .forms import FlashcardCheckAnswerModelForm
from .utils import check_answer
import random
import pickle

# Create your views here.
K = ['kot', 'pies', 'papuga']
L = ['cat', 'dog', 'parrot']


def home(request):
    form = FlashcardCheckAnswerModelForm(request.POST or None)
    check_answer_button = False
    text = ''

    with open('temporary_word.pkl', 'rb') as f:
        true_answer = pickle.load(f)

    if not true_answer[2]:
        i = random.choice(range(len(K)))
        word = K[i]
        with open('temporary_word.pkl', 'wb') as f:
            pickle.dump([L[i], K[i], True], f)
    else:
        word = None
        with open('temporary_word.pkl', 'wb') as f:
            pickle.dump([true_answer[0], true_answer[1], False], f)

    if form.is_valid():
        answer = form.cleaned_data.get('answer')
        form = FlashcardCheckAnswerModelForm()

        if not word:
            text = check_answer(true_answer[0], answer)

            form.fields['answer'].widget.attrs['disabled'] = 'disabled'
            form.fields['answer'].initial = true_answer[0]
            form.fields['answer'].widget.attrs['autofocus'] = False

            word = true_answer[1]
            check_answer_button = True

    if word is None:
        word = 'Click "check" button to start!'

    context = {
        'word': word,
        'check_answer_button': check_answer_button,
        'form': form,
        'text': text,
    }

    return render(request, 'flashcard.html', context)
