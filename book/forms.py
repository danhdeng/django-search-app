from django import forms


class PostSearchForm(forms.Form):
    q = forms.CharField(label="Search For")

    def __int__(self, *args, **kwargs):
        super(PostSearchForm, self).__init__(*args, **kwargs)
        self.fields["q"].label = "Search For"
        self.fields["q"].widget.attrs.update({"class": "form-control"})
