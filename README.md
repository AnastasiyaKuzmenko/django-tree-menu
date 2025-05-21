#  Django Tree Menu

This is a Django app that implements a **tree-structured menu system** with support for multiple named menus, nesting, active link highlighting, and admin-based editing.

## Features
✅ Menu is rendered via a **custom template tag**  
✅ All menu data is stored in the **database**  
✅ Menus are editable via the **Django admin interface**  
✅ **Multiple menus** can be rendered on a single page by name  
✅ Each menu item supports a **URL or named URL pattern**  
✅ The menu tree expands automatically to show the **active path**  
✅ The **active item is highlighted** based on the current page  
✅ Only **1 database query** is used per menu render 


## Folder Structure
```bash
.
├── config/                 # Django settings and configuration files (e.g., settings.py, urls.py)
│
├── db.sqlite3              # SQLite database file
│
├── Dockerfile              # Configuration for building the Docker image
│
├── entrypoint.sh           # Shell script used as the Docker container entry point
│
├── .gitignore            
│
├── manage.py             
├── menu/                   # Django app that implements the tree menu
│   ├── admin.py          
│   ├── apps.py           
│   ├── models.py           # Database models: Menu and MenuItem
│   ├── views.py
│   ├── static/
│     └── css/   
│        └── main.css       # Menu styling rules     
│   ├── templatetags/       # Custom template tags
│      └── menu_tags.py     # Custom template tag to render the tree menu
│   └── templates/          # HTML templates used by the app
│       ├── main.html       # Example base page that renders the menu
│       ├── menu.html       # Main menu template
│       └── menu_item.html  # Recursive template for nested menu items
│
├── requirements.txt        # List of Python dependencies
├── run_local.sh            # Activates venv, run migrations, and start the development server
└── README.md       

```

## Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/AnastasiyaKuzmenko/django-tree-menu.git
cd django-tree-menu
```
### 2. Create and activate a virtual environment
```bash
python3 -m venv venv
source ./venv/bin/activate
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Run the project
```bash
chmod +x run_local.sh
./run_local.sh
```
