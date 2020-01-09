from django.db import models
from django.contrib.postgres.fields import ArrayField
from ckeditor_uploader.fields import RichTextUploadingField

#save input, output file to "media/problem <id> / filename" directory
def path_to_save(instance, filename):
    return 'problem {0}/{1}'.format(instance.id, filename)

class Problem(models.Model):
    title = models.CharField(max_length=100, blank=False)
    difficulty = models.CharField(max_length=100)
    tags = ArrayField(models.CharField(max_length=100), blank = True)
    description = RichTextUploadingField()
    sample_input = RichTextUploadingField()
    sample_output = RichTextUploadingField()
    time_limit = ArrayField(models.IntegerField(default = 1)) #different time limit for different languages
    memory_limit = models.IntegerField(default = 256)
    input_file = models.FileField(upload_to = path_to_save)
    output_file = models.FileField(upload_to = path_to_save)
    no_of_submissions = models.IntegerField(default = 0)
    no_of_accepted = models.IntegerField(default = 0)
    
    def __str__(self):
        return str(self.id) + '. ' + self.title
    
	#copied from StackOverflow
    #override the default save for saving the files in designated folder. cause model has not created then. 
    def save(self, *args, **kwargs):
        if self.id is None:
            saved = []
            for f in self.__class__._meta.get_fields():
                if isinstance(f, models.FileField):
                    saved.append((f.name, getattr(self, f.name)))
                    setattr(self, f.name, None)

            super(self.__class__, self).save(*args, **kwargs)

            for name, val in saved:
                setattr(self, name, val)
        super(self.__class__, self).save(*args, **kwargs)


