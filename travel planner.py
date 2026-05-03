distance_mi=25
is_raining=False
has_bike=False
has_car=True
has_ride_share_app=False

if not bool(distance_mi):
    print(False)


if distance_mi<=1 and not(is_raining):
    print('True')
else:
    print('False')


if distance_mi>1 and distance_mi<=6:
    if has_bike and not is_raining:
        print('True')
    else:
        print('False')
elif distance_mi>6:
    if has_car and has_ride_share_app:
        print('True')
    else:
        print('False')
else:
    pass
