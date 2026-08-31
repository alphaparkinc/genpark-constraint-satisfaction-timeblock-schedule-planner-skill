from client import ConstraintSatisfactionTimeblockSchedulePlannerClient

def main():
    client = ConstraintSatisfactionTimeblockSchedulePlannerClient()
    res = client.plan_optimized_schedule(['Architecture RFC:120min:urgent', 'Team Sync:30min:low', 'Bug Triage:45min:medium'])
    print('Schedule Planner: ' + res['schedule_plan_id'] + ' (' + str(res['tasks_allocated_count']) + ' tasks)')
    print('Deep Work: ' + str(res['deep_work_focus_blocks_hours']) + ' hrs | Switching Penalty Reduction: ' + str(res['context_switching_penalty_reduced_pct']) + '%')
    print('Calendar ICS: ' + res['schedule_ics_calendar_url'])
    print('Notion DB: ' + res['notion_timeblock_database_url'])

if __name__ == '__main__':
    main()
