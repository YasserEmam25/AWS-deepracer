def reward_function(params):
    # Example of rewarding the agent to follow center line
    reward = 1.0

    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    objects_distance = params['objects_distance']
    is_offtrack = params['is_offtrack']
    is_crashed = params['is_crashed']
    speed = params['speed']

    # Calculate 3 markers that are at varying distances away from the center line
    # marker_1 = 0.1 * track_width
    # marker_2 = 0.25 * track_width
    # marker_3 = 0.5 * track_width

    # Give higher reward if the car is closer to center line and vice versa
    # if distance_from_center <= marker_1:
    #     reward = 1.0
    # elif distance_from_center <= marker_2:
    #     reward = 0.5
    # elif distance_from_center <= marker_3:
    #     reward = 0.1
    # else:
    #     reward = 1e-3 # likely crashed/ close to off track
        
    # treat the model when it moves greater distances in less time
    if len(objects_distance) >= 4:
        first = objects_distance[-1] - objects_distance[-2]
        second = objects_distance[-3] - objects_distance[-4]
        if first > second :
            reward *= (first - second) * 100.0
        elif first < second:
            reward *= (first - second) * 100.0
            
    # multiply the speed with the reward
    reward *= speed * 100.0
    
    # punish the model if it gets off-track
    if is_offtrack:
        reward = -10.0
    
    # punish the model if it gets crashed
    if is_crashed:
        reward = -10.0

    return float(reward)
