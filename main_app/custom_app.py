# A function to calculate cost of a task

def task_cost(profile, task, consumables):
    '''Takes profile, task, and an array of consumables and parameters.  Returns the sum of the profile hourly rate times the task duration and the cost of all of the consumables in the array.'''
    total_cost = profile.hourly_rate * task.duration
    for consumable in consumables:
        total_cost += consumable.cost
    return total_cost

    