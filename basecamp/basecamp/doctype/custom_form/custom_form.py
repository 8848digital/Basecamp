import frappe

def get_data():
    # Fetch attendance data from your ERPNext instance
    # Replace this with your logic to retrieve attendance data
    # Example: 
    # attendance_data = get_attendance_data_from_erpnext()

    # For demonstration purposes, let's create dummy data
    attendance_data = [
        {"date": "2023-12-01", "present": 30, "absent": 10},
        {"date": "2023-12-02", "present": 25, "absent": 15},
        # Add more data here...
    ]

    # Prepare data for the chart
    labels = []
    present = []
    absent = []

    for entry in attendance_data:
        labels.append(entry["date"])
        present.append(entry["present"])
        absent.append(entry["absent"])

    # Construct the chart data
    data = {
        "labels": labels,
        "datasets": [
            {
                "name": "Present",
                "values": present
            },
            {
                "name": "Absent",
                "values": absent
            }
        ]
    }

    return data

# Create the Chart document in Frappe
def create_attendance_chart():
    chart_data = get_data()

    chart = frappe.get_doc({
        "doctype": "Custom Form",
        "chart_type": "line",
        "label": "Attendance Chart",
        "data": chart_data
    })

    chart.insert(ignore_permissions=True)
    frappe.db.commit()

if __name__ == "__main__":
    create_attendance_chart()
