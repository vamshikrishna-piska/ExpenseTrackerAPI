ExpenseTracker API is a simple django restapi project allowing users to track their expenses with JWT Authentication.

Features=> 
User Registration & Authentication (JWT)
Manage Expenses (Create, Read, Update, Delete)
Expense Categories

Setup=>
1. Clone this repositoy first
git clone https://github.com/vamshikrishna-piska/ExpenseTrackerAPI.git
cd expense-tracker-api

2.Install the dependencies needed
pip install -r requirements.txt

3. Run migrations
python manage.py migrate

4. Create a superuser
python manage.py createsuperuser

5. Run the server
python manage.py runserver



API Endpoints=> Use postman for testing
POST /api/token/ - Obtain JWT token
POST /api/register/ - Register a new user
GET /api/expenses/ - View expenses
POST /api/expenses/ - Add an expense
GET /api/categories/ - View categories
