from powerbiclient import Report, models, ReportConnection

workspace_id = "bc7da3e9-213d-4afd-b9b9-6110aa239523"
report_id = "7e3748c5-143a-47f6-a4a5-2f493c33f803"
access_token = "your_access_token"

report = Report(workspace_id=workspace_id, report_id=report_id)
report_conn = ReportConnection(report, models.TokenType.Access, access_token)

report.refresh(report_conn)
