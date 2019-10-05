import json
from functools import lru_cache

from django.http import HttpResponse
from django.shortcuts import render
from time import perf_counter
# Create your views here.
from django.views import View


class Index(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        start_time = perf_counter()
        data = request.POST.dict()
        try:
            index = int(data['index'])
            fib_series = []
            for i in range(1, index+1):
                fib_series.append(fibonacci(i))
            nth_term = fib_series[index-1]

            end_time = perf_counter()
            response = {'nth_term': str(nth_term), 'time':end_time-start_time}
            return HttpResponse(json.dumps(response, default=str))
        except Exception as e:
            print(e)
            error = {'error': 'Please enter a valid positive integer'}
            return HttpResponse(json.dumps(error),status=422)



@lru_cache()
def fibonacci(n):
    if type(n) != int:
        raise TypeError()
    if n < 1:
        raise ValueError()

    if n == 1:
        return 1
    elif n==2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)
