class ConstraintSatisfactionTimeblockSchedulePlannerClient:
    def plan_optimized_schedule(self, tasks_specification=['Quarterly Earnings Call:60min:high', 'Code Review Sprint:90min:medium', 'Executive 1-on-1:45min:high'], daily_working_hours=8):
        return {
            'schedule_plan_id': 'sch_pln_8812',
            'tasks_allocated_count': len(tasks_specification),
            'deep_work_focus_blocks_hours': 4.5,
            'context_switching_penalty_reduced_pct': 72.4,
            'schedule_ics_calendar_url': 'https://schedule.genpark.ai/calendars/8812.ics',
            'notion_timeblock_database_url': 'https://schedule.genpark.ai/notion/8812.json'
        }
