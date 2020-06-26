from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DetailView
from .models import Submission

from collections import namedtuple, defaultdict


@login_required
def home(request):

    submissions_data = defaultdict(int)
    product_data = defaultdict(int)
    vendor_data = defaultdict(int)

    for vulnerability in Submission.objects.order_by('submission_date'):
        submissions_data[vulnerability.submission_date.year] += 1
        product_data[vulnerability.product_name] += 1
        vendor_data[vulnerability.vendor_name] += 1

    Year = namedtuple('Year', 'year, submissions_count')
    Product = namedtuple("Product", "name, count")
    Vendor = namedtuple("Vendor", "name, count")

    return render(request,
                  'submissions/home.html',
                  {"submissions_count_chart": [Year(year, sub_count) for year, sub_count in submissions_data.items()],
                   "product_distribution_chart": [Product(product, count) for product, count in product_data.items()],
                   "vendor_distribution_chart": [Vendor(vendor, count) for vendor, count in vendor_data.items()]})


@login_required
def about(request):
    return render(request, 'submissions/about.html')


class SubmissionCreateView(LoginRequiredMixin, CreateView):

    model = Submission
    fields = ['title', 'product_name', 'vendor_name', 'description_text', 'classification']

    def form_valid(self, form):
        form.instance.submitter = self.request.user
        return super().form_valid(form)


class SubmissionListView(LoginRequiredMixin, ListView):
    model = Submission
    template_name = 'submissions/entries.html'
    ordering = ['-submission_date']
    context_object_name = 'submissions'


class SubmissionDetailView(LoginRequiredMixin, DetailView):
    model = Submission
