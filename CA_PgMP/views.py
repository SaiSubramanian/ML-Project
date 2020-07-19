from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
import pandas as pd


class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'UI.html', context=None)


@csrf_exempt
def processPrediction(request):
    from ModelCode.RunLRmodel import trainModel
    from ModelCode.UserTest import predictProb
    fd, model = trainModel()
    inputData = []
    inputData.append('CONTRACT_COUNTRY_' + str(request.POST.get('contractCntry', None)))
    inputData.append('RQST_TYPE_DESC_' + str(request.POST.get('requestType', None)))
    inputData.append('COMPLEXITY_' + str(request.POST.get('complexity', None)))
    inputData.append('PROPOSAL_PRICING_TERMS_' + str(request.POST.get('proposalPricing', None)))
    inputData.append('SECTOR_' + str(request.POST.get('sector', None)))
    inputData.append('TXN_TYPE_DESC_' + str(request.POST.get('transactionType', None)))
    outputData = predictProb(fd, model, inputData)
    return HttpResponse(outputData)
