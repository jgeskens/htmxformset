from django.forms import modelformset_factory
from django.shortcuts import render, redirect
from django import forms
from django.utils.timezone import now

from . import models


class TodoItemForm(forms.ModelForm):
    """
    Customized TodoItem form.
    The `done` field is controlled by a checkbox form field `is_done`.
    """
    is_done = forms.BooleanField(required=False, label='Done')

    class Meta:
        model = models.TodoItem
        fields = ['done', 'is_done', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance:
            self.fields['is_done'].initial = bool(instance.done)

    def clean(self):
        cleaned_data = self.cleaned_data
        del cleaned_data['done']
        if cleaned_data['is_done'] and not self.instance.done:
            cleaned_data['done'] = now()
        if not cleaned_data['is_done'] and self.instance.done:
            cleaned_data['done'] = None
        return cleaned_data


def index(request):
    TodoItemFormSet = modelformset_factory(models.TodoItem, form=TodoItemForm, extra=1, can_delete=True)

    if request.method == 'POST':
        formset = TodoItemFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            if not request.htmx:
                return redirect(request.get_full_path())
            formset = TodoItemFormSet()
    else:
        formset = TodoItemFormSet()

    return render(request, 'hxformset/index.html', {'formset': formset})
