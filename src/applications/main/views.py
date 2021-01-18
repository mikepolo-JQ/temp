from django.views.generic import TemplateView


class IndexView(TemplateView):

    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        context.update({"ico": "g", "page": "index"})

        return context
