from django.test import TestCase

# Create your tests here.
from picturalizer.models import Image
img1 = Image.objects.get(title="ff")
img1.comments.all()