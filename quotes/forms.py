# import forms system for django
from django import forms
from .models import Stock

# create class for stock form
class StockForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ["ticker"] 