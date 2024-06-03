from django import forms




class SkinTypeForm(forms.Form):
    dry_skin = forms.ChoiceField(label='Do you feel your skin dry?', choices=[('Yes', 'Yes'), ('No', 'No')])
    oily_t_zone = forms.ChoiceField(label='Do you have excess sebum in the T-zone area?', choices=[('Yes', 'Yes'), ('No', 'No')])
    large_pores = forms.ChoiceField(label='Do you have enlarged pores?', choices=[('Yes', 'Yes'), ('No', 'No')])
    cold_feel = forms.ChoiceField(label='How does your skin feel in cold weather?', choices=[('Tight', 'It feels tight'), ('Normal', 'It feels normal')])
    cream_absorption = forms.ChoiceField(label='When you apply moisturizer, how quickly does it absorb into your skin?', choices=[('Fast', 'Fast'), ('Slow', 'Slow')])
    acne_prone = forms.ChoiceField(label='Do you have acne-prone skin?', choices=[('No acne', 'No, I don\'t have acne'), ('Few acne, maximum 5', 'Yes, I have a few acne, maximum 5'), ('Many acne, more than 10', 'Yes, I have quite a lot of acne, more than 10'), ('A lot of acne', 'Yes, I have a lot of acne')])
    irritated_skin = forms.ChoiceField(label='Does your skin get irritated if you don\'t use moisturizer?', choices=[('Yes', 'Yes'), ('No', 'No')])



class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput, min_length=5)

    
class AddUserForm(forms.Form):
    username = forms.CharField(max_length=30)
    password_1 = forms.CharField(widget=forms.PasswordInput, min_length=5, label="Password")
    password_2 = forms.CharField(widget=forms.PasswordInput, min_length=5, label="Re-enter password")
    name = forms.CharField(max_length=64)
    surname = forms.CharField(max_length=64)
    email = forms.EmailField(max_length=64)


class ResetPasswordForm(forms.Form):
    password_1 = forms.CharField(widget=forms.PasswordInput, min_length=5, label="Password")
    password_2 = forms.CharField(widget=forms.PasswordInput, min_length=5, label="Re-enter password")
