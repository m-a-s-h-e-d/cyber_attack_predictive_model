# pages/views.py
import pickle
import pandas as pd
import tensorflow as tf

from django.shortcuts import render, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.views.generic import TemplateView


def homePost(request):
    # Use request object to extract choice.

    rst_count = -999
    urg_count = -999
    flow_duration = -999
    duration = -999
    weight = -999
    variance = -999

    try:
        # Extract value from request object by control name. 
        rst_count = request.POST['rst_count']
        urg_count = request.POST['urg_count']
        flow_duration = request.POST['flow_duration']
        duration = request.POST['duration']
        weight = request.POST['weight']
        variance = request.POST['variance']

        # Request received
        print("New request received:")
        print("rst_count: " + rst_count)
        print("urg_count: " + urg_count)
        print("flow_duration: " + flow_duration)
        print("duration: " + duration)
        print("weight: " + weight)
        print("variance: " + variance)
        rst_count = float(rst_count)
        urg_count = float(urg_count)
        flow_duration = float(flow_duration)
        duration = float(duration)
        weight = float(weight)
        variance = float(variance)
        
    # Enters 'except' block if unable to parse.
    except:
        return render(request, 'home.html', {
                'errorMessage':'*** The data submitted is invalid. Please try again.'
            })
    else:
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('results', kwargs={'rst_count': rst_count,
                                                               'urg_count': urg_count,
                                                               'flow_duration': flow_duration,
                                                               'duration': duration,
                                                               'weight': weight,
                                                               'variance': variance}))
    

def results(request, rst_count, urg_count, flow_duration, duration, weight, variance):
    print("*** Inside results()")
    # load saved model
    loadedModel = tf.keras.models.load_model('model.keras')

    # Create a single prediction.
    singleSampleDf = pd.DataFrame(columns=['rst_count', 'urg_count', 'flow_duration', 'Duration', 'Weight', 'Variance'])

    # Extract value from request object by control name.
    rst_count = float(rst_count)
    urg_count = float(urg_count)
    flow_duration = float(flow_duration)
    duration = float(duration)
    weight = float(weight)
    variance = float(variance)
    singleSampleDf = singleSampleDf._append({'rst_count': rst_count,
                                            'urg_count': urg_count,
                                            'flow_duration': flow_duration,
                                            'Duration': duration,
                                            'Weight': weight,
                                            'Variance': variance}, ignore_index=True)

    singlePrediction = loadedModel.predict(singleSampleDf)
    singlePrediction = round(singlePrediction[0][0])

    print("Single prediction: " + str(singlePrediction))

    return render(request, 'results.html', {'rst_count': rst_count,
                                            'urg_count': urg_count,
                                            'flow_duration': flow_duration,
                                            'duration': duration,
                                            'weight': weight,
                                            'variance': variance,
                                            'prediction':singlePrediction})



def homePageView(request):
    # return request object and specify page.
    return render(request, 'home.html', {'firstName': 'Mashed',
                                         'lastName': 'Dev'}) 
