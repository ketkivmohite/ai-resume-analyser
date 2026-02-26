from django.db import models
import fitz

class Resume(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to="resumes/", null=True, blank=True)
    extracted_text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.file:
            pdf_path = self.file.path
            doc = fitz.open(pdf_path)
            text = ""

            for page in doc:
                text += page.get_text()

            self.extracted_text = text
            super().save(update_fields=["extracted_text"])