current_milestone = (current_followers//milestone_increment)

progress_in_milestone = (current_follower%milestone_increment)

total_gained = (current_followers - starting_followers)
daily_average = (total_gained// days_tracked)
days_to_milestone (milestone_incerment - progress_in_milestone)// daily_average
weekly_growth = (daily_average * 7)

print(f"Creator: {Creator_name}")
print(f"Current Milestone: {current_milestone}")
print(f"Progress in Milestone: {progress_in_milestone} followers")
print(f"Total Growth: {total_growth} followers")
print(f"Daily Average: {daily_average} followers")
print(f"Days to Next Milestone: {days_to_next_milestone} days")
print(f"Weekly Growth Projection: {weekly_growth_projections} follwers"
