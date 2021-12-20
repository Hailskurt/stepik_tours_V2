from django.shortcuts import render
import tours.data as data
import random


tours = data.tours


def main_view(request):
    keys = random.sample(list(tours.keys()), 6)
    random_tours = []
    for key in keys:
        random_tours.append(tours[key])
    return render(request, 'index.html', {'tours': random_tours,
                                          'title': data.title,
                                          'subtitle': data.subtitle,
                                          'description': data.description,
                                          'keys': keys})


def departure_view(request, departure):
    matched_tours = []
    max_price = 0
    min_price = float('inf')
    max_time = 0
    min_time = float('inf')
    for key in tours.keys():
        if tours[key]['departure'] == departure:
            matched_tours.append(tours[key])
            matched_tours[-1]['key'] = key
    for tour in matched_tours:
        if tour['price'] > max_price:
            max_price = tour['price']
        if tour['price'] < min_price:
            min_price = tour['price']
        if tour['nights'] > max_time:
            max_time = tour['nights']
        if tour['nights'] < min_time:
            min_time = tour['nights']

    return render(request, 'departure.html', {'departure': data.departures[departure][3:],
                                              'tours': matched_tours,
                                              'count': len(matched_tours),
                                              'max_price': max_price,
                                              'min_price': min_price,
                                              'max_time': max_time,
                                              'min_time': min_time})


def tour_view(request, tour_id):
    return render(request, 'tour.html', tours[tour_id])
