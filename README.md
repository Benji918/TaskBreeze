# Django-Task-Manager
A Django REST API application for users to manage and assign tasks 
# Link to architectural diagram
https://lucid.app/lucidchart/b8b56bc8-ffa4-4253-990a-3a2638e46676/edit?viewport_loc=-9273%2C-4244%2C16513%2C7542%2CmF6v7kzw-swz&invitationId=inv_d74a2024-32c8-4c5e-b53e-99ff1f251dd4
![](https://github.com/Benji918/Django-Task-Manager/blob/main/TASK%20MANAGEMENT%20SYSTEM.jpeg)

https://dbdiagram.io/d/TaskBreeze-ER-diagram-6592f36cac844320ae0f568f
![](https://github.com/Benji918/TaskBreeze/blob/main/TaskBreeze%20ER%20diagram.png)


# Proposed Features
**Basic Features:**

1. **User Authentication and Authorization:**
   - Implement a robust user authentication system using Django's built-in authentication or a third-party package like Django REST Framework JWT.
   - Define user roles and permissions to control access to different API endpoints.

2. **Task CRUD Operations:**
   - Create, read, update, and delete tasks using the RESTful API.
   - Allow users to add, modify, and remove tasks from their lists.

3. **Task Lists Management:**
   - Create, read, update, and delete task lists.
   - Allow users to organize their tasks into different lists.

4. **Task Prioritization:**
   - Implement a system for prioritizing tasks, such as using a priority field or a drag-and-drop interface.

5. **Task Due Dates and Reminders:**
   - Allow users to set due dates and reminders for their tasks.
   - Send email or push notifications to remind users about upcoming deadlines.

6. **Task Comments:**
   - Enable users to add comments to tasks for collaboration and discussion.

7. **Task Attachments:**
   - Allow users to attach files to their tasks for reference or sharing.

8. **Task History:**
   - Keep a record of task changes, such as updates to the task title, description, or status.

**Advanced Features:**

1. **Task Templates:**
   - Allow users to create task templates with predefined titles, descriptions, and due dates.

2. **Task Recurrence:**
   - Implement a feature for recurring tasks that can be repeated daily, weekly, monthly, or yearly.

3. **Task Dependencies:**
   - Enable users to create dependencies between tasks, so that one task cannot be completed until another task is finished.

4. **Task Collaboration:**
   - Allow multiple users to collaborate on tasks, assign tasks to each other, and track their progress.

5. **Task Reporting:**
   - Generate reports on task completion rates, overdue tasks, and task trends over time.

6. **Task Integration with Other Systems:**
   - Integrate the task management system with other productivity tools, such as calendar apps or email clients.

7. **Task Automation:**
   - Implement automated workflows to trigger certain actions based on task events, such as sending notifications or updating task statuses.

8. **Task Analytics:**
   - Collect and analyze data on task completion times, task dependencies, and user productivity to identify areas for improvement.

**User Features:**

* Create, read, update, and delete their own tasks.
* Create, read, update, and delete their own task lists.
* Prioritize their tasks.
* Set due dates and reminders for their tasks.
* Add comments to tasks.
* Attach files to tasks.
* View their own task history.
* Collaborate on tasks with other users (if enabled by the admin).
* View task reports (if enabled by the admin).

**Admin Features:**

* Create, read, update, and delete all tasks and task lists.
* Prioritize tasks for all users.
* Set due dates and reminders for tasks for all users.
* Add comments to tasks for all users.
* Attach files to tasks for all users.
* View the task history for all users.
* Manage user accounts, including creating, editing, and deleting users.
* Assign user roles and permissions.
* Configure system settings, such as default task priorities and due date reminders.
* Generate task reports for all users.
* Integrate the task management system with other systems, such as calendar apps or email clients.
* Manage automated workflows for task events.
* Analyze task data to identify areas for improvement.

In addition to the above, admins may also have the ability to:

* Create and manage task templates.
* Enable or disable task recurrence.
* Enable or disable task dependencies.
* Enable or disable task collaboration.
* Customize the task management system's user interface and branding.
