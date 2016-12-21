from django import forms

class LinkForm(forms.Form):
    """
    Form for individual user links
    """
    anchor = forms.CharField(
                    max_length=100,
                    widget=forms.TextInput(attrs={
                        'placeholder': 'Link Name / Anchor Text',
                    }),
                    required=False)
    url = forms.URLField(
                    widget=forms.URLInput(attrs={
                        'placeholder': 'URL',
                    }),
                    required=False)

    class ProfileForm(forms.Form):
        """
        Form for user to update their own profile details
        (excluding links which are handled by a separate formset)
        """

        def __init__(self, *args, **kwargs):
            self.user = kwargs.pop('user', None)
            super(ProfileForm, self).__init__(*args, **kwargs)

            self.fields['first_name'] = forms.CharField(
                max_length=30,
                initial=self.user.first_name,
                widget=forms.TextInput(attrs={
                    'placeholder': 'First Name',
                }))
            self.fields['last_name'] = forms.CharField(
                max_length=30,
                initial=self.user.last_name,
                widget=forms.TextInput(attrs={
                    'placeholder': 'Last Name',
                }))
