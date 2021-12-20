from django.shortcuts import render
import tours.data as data
import random

tours = data.tours


def main_view(request):
    keys = random.sample(list(tours.keys()), 6)
    random_tours = []
    for key in keys:
        random_tours.append(tours[key])
        random_tours[-1]['key'] = key
    return render(request, 'index.html', {'tours': random_tours,
                                          'title': data.title,
                                          'subtitle': data.subtitle,
                                          'description': data.description,
                                          'keys': keys,
                                          'departures': data.departures})


def departure_view(request, departure):
    matched_tours = []
    for key in tours.keys():
        if tours[key]['departure'] == departure:
            matched_tours.append(tours[key])
            matched_tours[-1]['key'] = key
    max_time = max(tour['nights'] for tour in matched_tours)
    min_time = min(tour['nights'] for tour in matched_tours)
    max_price = max(tour['price'] for tour in matched_tours)
    min_price = min(tour['price'] for tour in matched_tours)

    return render(request, 'departure.html', {'departure': data.departures[departure][3:],
                                              'tours': matched_tours,
                                              'count': len(matched_tours),
                                              'max_price': max_price,
                                              'min_price': min_price,
                                              'max_time': max_time,
                                              'min_time': min_time,
                                              'departures': data.departures})


def tour_view(request, tour_id):
    return render(request, 'tour.html', {'tour': tours[tour_id]})
