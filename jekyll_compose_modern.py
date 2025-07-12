#!/usr/bin/env python3
"""
Jekyll Compose GUI - Ultra Modern Edition
A sleek, modern GUI application for Jekyll content creation with simplified codebase.
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import re
import yaml
from datetime import datetime
import subprocess
import webbrowser
from pathlib import Path
import json

class ModernJekyllGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.setup_window()
        self.setup_variables()
        self.setup_modern_style()
        self.create_modern_ui()
        self.load_site()
    
    def setup_window(self):
        """Configure main window"""
        self.root.title("Jekyll Compose - Modern")
        self.root.geometry("1000x700")
        self.root.minsize(800, 600)
        
        # Modern window styling
        try:
            self.root.tk.call('tk', 'scaling', 1.5)  # Better DPI scaling
        except:
            pass
    
    def setup_variables(self):
        """Initialize application variables"""
        self.jekyll_root = self.find_jekyll_root()
        self.config = self.load_config()
        self.status_var = tk.StringVar(value="Ready")
        self.auto_open_var = tk.BooleanVar(value=self.config.get('auto_open', False))
    
    def setup_modern_style(self):
        """Configure modern visual theme"""
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Modern color scheme
        self.colors = {
            'primary': '#2563eb',      # Blue
            'secondary': '#64748b',    # Slate
            'success': '#10b981',      # Green
            'warning': '#f59e0b',      # Amber
            'danger': '#ef4444',       # Red
            'bg_light': '#f8fafc',     # Light gray
            'bg_card': '#ffffff',      # White
            'text_primary': '#1e293b', # Dark slate
            'text_secondary': '#64748b' # Medium slate
        }
        
        # Configure modern styles
        self.configure_styles()
    
    def configure_styles(self):
        """Apply modern styling to ttk widgets"""
        # Configure modern button style
        self.style.configure('Modern.TButton',
                            background=self.colors['primary'],
                            foreground='white',
                            borderwidth=0,
                            focuscolor='none',
                            padding=(20, 10))
        
        self.style.map('Modern.TButton',
                      background=[('active', '#1d4ed8'),
                                ('pressed', '#1e40af')])
        
        # Secondary button style
        self.style.configure('Secondary.TButton',
                            background=self.colors['bg_light'],
                            foreground=self.colors['text_primary'],
                            borderwidth=1,
                            relief='solid',
                            focuscolor='none',
                            padding=(15, 8))
        
        # Modern frame styles
        self.style.configure('Card.TFrame',
                            background=self.colors['bg_card'],
                            relief='flat',
                            borderwidth=1)
        
        # Modern label styles
        self.style.configure('Title.TLabel',
                            font=('Segoe UI', 24, 'bold'),
                            foreground=self.colors['text_primary'],
                            background=self.colors['bg_light'])
        
        self.style.configure('Heading.TLabel',
                            font=('Segoe UI', 14, 'bold'),
                            foreground=self.colors['text_primary'])
        
        self.style.configure('Body.TLabel',
                            font=('Segoe UI', 10),
                            foreground=self.colors['text_secondary'])
    
    def create_modern_ui(self):
        """Create the modern user interface"""
        # Configure root
        self.root.configure(bg=self.colors['bg_light'])
        
        # Main container with modern styling
        main_container = tk.Frame(self.root, bg=self.colors['bg_light'])
        main_container.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Header section
        self.create_header(main_container)
        
        # Content area with sidebar and main content
        content_frame = tk.Frame(main_container, bg=self.colors['bg_light'])
        content_frame.pack(fill='both', expand=True, pady=(20, 0))
        
        # Sidebar
        self.create_sidebar(content_frame)
        
        # Main content area
        self.create_main_content(content_frame)
        
        # Footer with status
        self.create_footer(main_container)
    
    def create_header(self, parent):
        """Create modern header section"""
        header = tk.Frame(parent, bg=self.colors['bg_light'], height=80)
        header.pack(fill='x', pady=(0, 20))
        header.pack_propagate(False)
        
        # Title and subtitle
        title_frame = tk.Frame(header, bg=self.colors['bg_light'])
        title_frame.pack(side='left', fill='y')
        
        title = ttk.Label(title_frame, text="Jekyll Compose", style='Title.TLabel')
        title.pack(anchor='w')
        
        subtitle = ttk.Label(title_frame, text="Modern content creation for Jekyll sites", 
                            style='Body.TLabel')
        subtitle.pack(anchor='w')
        
        # Quick actions
        actions_frame = tk.Frame(header, bg=self.colors['bg_light'])
        actions_frame.pack(side='right', fill='y')
        
        ttk.Button(actions_frame, text="🚀 Serve Site", style='Modern.TButton',
                  command=self.serve_site).pack(side='right', padx=(5, 0))
        ttk.Button(actions_frame, text="🔧 Build", style='Secondary.TButton',
                  command=self.build_site).pack(side='right', padx=(5, 0))
        ttk.Button(actions_frame, text="📁 Open Folder", style='Secondary.TButton',
                  command=self.open_folder).pack(side='right', padx=(5, 0))
    
    def create_sidebar(self, parent):
        """Create modern sidebar navigation"""
        sidebar = tk.Frame(parent, bg=self.colors['bg_card'], width=250)
        sidebar.pack(side='left', fill='y', padx=(0, 20))
        sidebar.pack_propagate(False)
        
        # Add shadow effect (border)
        sidebar.configure(relief='solid', bd=1, highlightbackground=self.colors['secondary'])
        
        # Jekyll root section
        self.create_root_section(sidebar)
        
        # Navigation menu
        self.create_navigation(sidebar)
        
        # File browser
        self.create_file_browser(sidebar)
    
    def create_root_section(self, parent):
        """Create Jekyll root selection section"""
        root_frame = tk.Frame(parent, bg=self.colors['bg_card'])
        root_frame.pack(fill='x', padx=15, pady=15)
        
        ttk.Label(root_frame, text="Jekyll Site", style='Heading.TLabel').pack(anchor='w')
        
        # Path display
        path_frame = tk.Frame(root_frame, bg=self.colors['bg_light'], relief='solid', bd=1)
        path_frame.pack(fill='x', pady=(5, 10))
        
        self.path_label = tk.Label(path_frame, text=self.jekyll_root, 
                                  bg=self.colors['bg_light'], fg=self.colors['text_secondary'],
                                  font=('Consolas', 9), anchor='w', padx=10, pady=5)
        self.path_label.pack(fill='x')
        
        ttk.Button(root_frame, text="Change Location", style='Secondary.TButton',
                  command=self.change_root).pack(fill='x')
    
    def create_navigation(self, parent):
        """Create navigation menu"""
        nav_frame = tk.Frame(parent, bg=self.colors['bg_card'])
        nav_frame.pack(fill='x', padx=15, pady=(0, 15))
        
        ttk.Label(nav_frame, text="Quick Actions", style='Heading.TLabel').pack(anchor='w', pady=(0, 10))
        
        # Navigation buttons with icons
        nav_items = [
            ("✏️ New Post", self.new_post),
            ("📝 New Draft", self.new_draft),
            ("📄 New Page", self.new_page),
            ("📚 Collection File", self.new_collection),
            ("🚀 Publish Draft", self.publish_draft),
            ("📦 Unpublish Post", self.unpublish_post),
        ]
        
        for text, command in nav_items:
            btn = tk.Button(nav_frame, text=text, command=command,
                           bg=self.colors['bg_light'], fg=self.colors['text_primary'],
                           border=0, font=('Segoe UI', 10), anchor='w', padx=15, pady=8,
                           activebackground=self.colors['primary'], activeforeground='white')
            btn.pack(fill='x', pady=1)
            
            # Hover effects
            btn.bind('<Enter>', lambda e, b=btn: b.configure(bg=self.colors['primary'], fg='white'))
            btn.bind('<Leave>', lambda e, b=btn: b.configure(bg=self.colors['bg_light'], fg=self.colors['text_primary']))
    
    def create_file_browser(self, parent):
        """Create compact file browser"""
        browser_frame = tk.Frame(parent, bg=self.colors['bg_card'])
        browser_frame.pack(fill='both', expand=True, padx=15, pady=(0, 15))
        
        ttk.Label(browser_frame, text="Recent Files", style='Heading.TLabel').pack(anchor='w', pady=(0, 10))
        
        # File list
        self.file_listbox = tk.Listbox(browser_frame, 
                                      bg=self.colors['bg_light'],
                                      fg=self.colors['text_primary'],
                                      selectbackground=self.colors['primary'],
                                      selectforeground='white',
                                      border=0, font=('Segoe UI', 9))
        self.file_listbox.pack(fill='both', expand=True)
        self.file_listbox.bind('<Double-Button-1>', lambda e: self.open_selected_file())
        
        self.refresh_files()
    
    def create_main_content(self, parent):
        """Create main content area"""
        self.content_area = tk.Frame(parent, bg=self.colors['bg_light'])
        self.content_area.pack(side='right', fill='both', expand=True)
        
        # Welcome screen
        self.show_welcome()
    
    def show_welcome(self):
        """Show welcome screen"""
        # Clear content area
        for widget in self.content_area.winfo_children():
            widget.destroy()
        
        welcome_frame = tk.Frame(self.content_area, bg=self.colors['bg_card'], relief='solid', bd=1)
        welcome_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Center content
        center_frame = tk.Frame(welcome_frame, bg=self.colors['bg_card'])
        center_frame.place(relx=0.5, rely=0.5, anchor='center')
        
        # Welcome content
        welcome_icon = tk.Label(center_frame, text="🎯", font=('Segoe UI', 48),
                               bg=self.colors['bg_card'])
        welcome_icon.pack(pady=(0, 20))
        
        welcome_title = tk.Label(center_frame, text="Welcome to Jekyll Compose",
                                font=('Segoe UI', 20, 'bold'),
                                fg=self.colors['text_primary'], bg=self.colors['bg_card'])
        welcome_title.pack(pady=(0, 10))
        
        welcome_text = tk.Label(center_frame, 
                               text="Create and manage your Jekyll content with ease.\nChoose an action from the sidebar to get started.",
                               font=('Segoe UI', 12), fg=self.colors['text_secondary'],
                               bg=self.colors['bg_card'], justify='center')
        welcome_text.pack(pady=(0, 30))
        
        # Quick start buttons
        quick_frame = tk.Frame(center_frame, bg=self.colors['bg_card'])
        quick_frame.pack()
        
        ttk.Button(quick_frame, text="📝 Create Post", style='Modern.TButton',
                  command=self.new_post).pack(side='left', padx=(0, 10))
        ttk.Button(quick_frame, text="📄 Create Page", style='Secondary.TButton',
                  command=self.new_page).pack(side='left')
    
    def create_footer(self, parent):
        """Create footer with status bar"""
        footer = tk.Frame(parent, bg=self.colors['bg_card'], height=40, relief='solid', bd=1)
        footer.pack(fill='x', pady=(20, 0))
        footer.pack_propagate(False)
        
        # Status indicator
        status_frame = tk.Frame(footer, bg=self.colors['bg_card'])
        status_frame.pack(side='left', fill='y', padx=15)
        
        status_dot = tk.Label(status_frame, text="●", fg=self.colors['success'],
                             bg=self.colors['bg_card'], font=('Segoe UI', 12))
        status_dot.pack(side='left', pady=10)
        
        status_label = tk.Label(status_frame, textvariable=self.status_var,
                               fg=self.colors['text_secondary'], bg=self.colors['bg_card'],
                               font=('Segoe UI', 10))
        status_label.pack(side='left', padx=(5, 0), pady=10)
        
        # Settings
        settings_frame = tk.Frame(footer, bg=self.colors['bg_card'])
        settings_frame.pack(side='right', fill='y', padx=15)
        
        ttk.Checkbutton(settings_frame, text="Auto-open files", 
                       variable=self.auto_open_var,
                       command=self.save_settings).pack(side='right', pady=10)
    
    def show_form(self, title, fields, callback):
        """Show modern form dialog"""
        # Clear content area
        for widget in self.content_area.winfo_children():
            widget.destroy()
        
        form_frame = tk.Frame(self.content_area, bg=self.colors['bg_card'], relief='solid', bd=1)
        form_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Form header
        header_frame = tk.Frame(form_frame, bg=self.colors['primary'], height=60)
        header_frame.pack(fill='x')
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(header_frame, text=title, 
                              font=('Segoe UI', 16, 'bold'), fg='white', bg=self.colors['primary'])
        title_label.pack(expand=True)
        
        # Form content
        content_frame = tk.Frame(form_frame, bg=self.colors['bg_card'])
        content_frame.pack(fill='both', expand=True, padx=40, pady=40)
        
        # Form fields
        field_vars = {}
        for i, (field_name, field_type, default) in enumerate(fields):
            field_frame = tk.Frame(content_frame, bg=self.colors['bg_card'])
            field_frame.pack(fill='x', pady=(0, 20))
            
            label = tk.Label(field_frame, text=field_name,
                           font=('Segoe UI', 12, 'bold'), fg=self.colors['text_primary'],
                           bg=self.colors['bg_card'])
            label.pack(anchor='w', pady=(0, 5))
            
            if field_type == 'text':
                var = tk.StringVar(value=default)
                entry = tk.Entry(field_frame, textvariable=var, font=('Segoe UI', 11),
                               relief='solid', bd=1, bg=self.colors['bg_light'])
                entry.pack(fill='x', ipady=8)
                if i == 0:  # Focus first field
                    entry.focus()
            elif field_type == 'combo':
                var = tk.StringVar(value=default[0] if default else '')
                combo = ttk.Combobox(field_frame, textvariable=var, values=default or [],
                                   font=('Segoe UI', 11))
                combo.pack(fill='x', ipady=8)
            
            field_vars[field_name] = var
        
        # Buttons
        button_frame = tk.Frame(content_frame, bg=self.colors['bg_card'])
        button_frame.pack(fill='x', pady=(20, 0))
        
        ttk.Button(button_frame, text="Cancel", style='Secondary.TButton',
                  command=self.show_welcome).pack(side='right', padx=(10, 0))
        ttk.Button(button_frame, text="Create", style='Modern.TButton',
                  command=lambda: self.handle_form_submit(field_vars, callback)).pack(side='right')
    
    def handle_form_submit(self, field_vars, callback):
        """Handle form submission"""
        values = {name: var.get().strip() for name, var in field_vars.items()}
        
        # Validate required fields
        if not values.get('Title'):
            messagebox.showwarning("Validation Error", "Title is required")
            return
        
        # Call the callback with form values
        callback(values)
        self.show_welcome()
    
    # Content creation methods
    def new_post(self):
        """Create new post form"""
        fields = [
            ('Title', 'text', ''),
            ('Date', 'text', datetime.now().strftime('%Y-%m-%d')),
            ('Format', 'text', '%Y-%m-%d')
        ]
        self.show_form("✏️ Create New Post", fields, self._create_post)
    
    def new_draft(self):
        """Create new draft form"""
        fields = [('Title', 'text', '')]
        self.show_form("📝 Create New Draft", fields, self._create_draft)
    
    def new_page(self):
        """Create new page form"""
        fields = [('Title', 'text', '')]
        self.show_form("📄 Create New Page", fields, self._create_page)
    
    def new_collection(self):
        """Create new collection file form"""
        collections = self.get_collections()
        fields = [
            ('Title', 'text', ''),
            ('Collection', 'combo', collections)
        ]
        self.show_form("📚 Create Collection File", fields, self._create_collection)
    
    def _create_post(self, values):
        """Create post with values"""
        date = values['Date'] or datetime.now().strftime('%Y-%m-%d')
        path = self.create_file('_posts', values['Title'], date, 'posts')
        if path:
            self.update_status(f"✓ Post created: {Path(path).name}")
            self.refresh_files()
    
    def _create_draft(self, values):
        """Create draft with values"""
        path = self.create_file('_drafts', values['Title'], None, 'drafts')
        if path:
            self.update_status(f"✓ Draft created: {Path(path).name}")
            self.refresh_files()
    
    def _create_page(self, values):
        """Create page with values"""
        path = self.create_file('_pages', values['Title'], None, 'pages')
        if path:
            self.update_status(f"✓ Page created: {Path(path).name}")
            self.refresh_files()
    
    def _create_collection(self, values):
        """Create collection file with values"""
        if not values['Collection']:
            messagebox.showwarning("Error", "Please select a collection")
            return
        path = self.create_file(f"_{values['Collection']}", values['Title'], None, values['Collection'])
        if path:
            self.update_status(f"✓ Collection file created: {Path(path).name}")
            self.refresh_files()
    
    # Utility methods (simplified)
    def find_jekyll_root(self):
        """Find Jekyll root directory"""
        current = Path.cwd()
        for path in [current] + list(current.parents):
            if (path / '_config.yml').exists():
                return str(path)
        return str(current)
    
    def load_config(self):
        """Load configuration"""
        config_file = Path(self.jekyll_root) / '.jekyll_gui_config.json'
        try:
            if config_file.exists():
                with open(config_file) as f:
                    return json.load(f)
        except:
            pass
        return {}
    
    def save_settings(self):
        """Save application settings"""
        config = {'auto_open': self.auto_open_var.get()}
        config_file = Path(self.jekyll_root) / '.jekyll_gui_config.json'
        try:
            with open(config_file, 'w') as f:
                json.dump(config, f)
        except:
            pass
    
    def get_collections(self):
        """Get available collections"""
        collections = ['posts', 'drafts', 'pages']
        jekyll_path = Path(self.jekyll_root)
        for item in jekyll_path.iterdir():
            if (item.is_dir() and item.name.startswith('_') and 
                item.name not in ['_site', '_sass', '_layouts', '_includes', '_data']):
                collections.append(item.name[1:])
        return sorted(set(collections))
    
    def slugify(self, title):
        """Convert title to slug"""
        slug = re.sub(r'[^\w\s-]', '', title.lower())
        return re.sub(r'[-\s]+', '-', slug).strip('-')
    
    def create_file(self, folder, title, date=None, content_type='posts'):
        """Create Jekyll file"""
        try:
            folder_path = Path(self.jekyll_root) / folder
            folder_path.mkdir(exist_ok=True)
            
            slug = self.slugify(title)
            filename = f"{date}-{slug}.md" if date else f"{slug}.md"
            file_path = folder_path / filename
            
            if file_path.exists() and not messagebox.askyesno("File Exists", f"Overwrite {filename}?"):
                return None
            
            # Simple front matter
            front_matter = f"---\ntitle: {title}\n"
            if date:
                front_matter += f"date: {date}\n"
            front_matter += "---\n\n"
            
            file_path.write_text(front_matter, encoding='utf-8')
            
            if self.auto_open_var.get():
                self.open_file(file_path)
            
            return str(file_path)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create file: {e}")
            return None
    
    def refresh_files(self):
        """Refresh file list"""
        self.file_listbox.delete(0, tk.END)
        
        # Get recent files from posts and drafts
        files = []
        for folder in ['_posts', '_drafts', '_pages']:
            folder_path = Path(self.jekyll_root) / folder
            if folder_path.exists():
                for file_path in folder_path.glob('*.md'):
                    files.append((file_path.stat().st_mtime, file_path.name, str(file_path)))
        
        # Sort by modification time and show recent 20
        files.sort(reverse=True)
        for _, name, path in files[:20]:
            self.file_listbox.insert(tk.END, name)
    
    def open_selected_file(self):
        """Open selected file"""
        selection = self.file_listbox.curselection()
        if selection:
            filename = self.file_listbox.get(selection[0])
            # Find the file path
            for folder in ['_posts', '_drafts', '_pages']:
                file_path = Path(self.jekyll_root) / folder / filename
                if file_path.exists():
                    self.open_file(file_path)
                    break
    
    def open_file(self, file_path):
        """Open file in default editor"""
        try:
            if os.name == 'nt':
                os.startfile(file_path)
            else:
                subprocess.run(['open' if os.uname().sysname == 'Darwin' else 'xdg-open', str(file_path)])
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open file: {e}")
    
    def open_folder(self):
        """Open Jekyll folder"""
        self.open_file(self.jekyll_root)
    
    def change_root(self):
        """Change Jekyll root"""
        new_root = filedialog.askdirectory(title="Select Jekyll Root", initialdir=self.jekyll_root)
        if new_root:
            self.jekyll_root = new_root
            self.path_label.config(text=new_root)
            self.refresh_files()
            self.update_status(f"📁 Changed to: {Path(new_root).name}")
    
    def publish_draft(self):
        """Quick publish draft"""
        drafts_path = Path(self.jekyll_root) / "_drafts"
        if not drafts_path.exists():
            messagebox.showinfo("Info", "No drafts folder found")
            return
        
        drafts = list(drafts_path.glob("*.md"))
        if not drafts:
            messagebox.showinfo("Info", "No drafts found")
            return
        
        # Show simple selection dialog
        dialog = ModernListDialog(self.root, "Select Draft to Publish", 
                                 [d.name for d in drafts])
        if dialog.result is not None:
            draft_file = drafts[dialog.result]
            date = datetime.now().strftime('%Y-%m-%d')
            
            # Move and rename file
            content = draft_file.read_text(encoding='utf-8')
            title_match = re.search(r'^title:\s*(.+)$', content, re.MULTILINE)
            title = title_match.group(1).strip().strip('"\'') if title_match else draft_file.stem
            
            slug = self.slugify(title)
            post_path = Path(self.jekyll_root) / "_posts" / f"{date}-{slug}.md"
            post_path.parent.mkdir(exist_ok=True)
            
            # Add date to front matter if not present
            if 'date:' not in content:
                content = content.replace('---\n', f'---\ndate: {date}\n', 1)
            
            post_path.write_text(content, encoding='utf-8')
            draft_file.unlink()
            
            self.update_status(f"🚀 Published: {post_path.name}")
            self.refresh_files()
    
    def unpublish_post(self):
        """Quick unpublish post"""
        posts_path = Path(self.jekyll_root) / "_posts"
        if not posts_path.exists():
            messagebox.showinfo("Info", "No posts folder found")
            return
        
        posts = list(posts_path.glob("*.md"))
        if not posts:
            messagebox.showinfo("Info", "No posts found")
            return
        
        dialog = ModernListDialog(self.root, "Select Post to Unpublish", 
                                 [p.name for p in posts])
        if dialog.result is not None:
            post_file = posts[dialog.result]
            
            # Remove date prefix and move to drafts
            name_parts = post_file.name.split('-', 3)
            new_name = name_parts[3] if len(name_parts) >= 4 else post_file.name
            
            drafts_path = Path(self.jekyll_root) / "_drafts"
            drafts_path.mkdir(exist_ok=True)
            draft_path = drafts_path / new_name
            
            draft_path.write_text(post_file.read_text(encoding='utf-8'), encoding='utf-8')
            post_file.unlink()
            
            self.update_status(f"📦 Unpublished: {draft_path.name}")
            self.refresh_files()
    
    def build_site(self):
        """Build Jekyll site"""
        self.run_jekyll_command("build")
    
    def serve_site(self):
        """Serve Jekyll site"""
        self.run_jekyll_command("serve")
    
    def run_jekyll_command(self, command):
        """Run Jekyll command"""
        try:
            cmd = f"bundle exec jekyll {command}"
            if os.name == 'nt':
                subprocess.Popen(f'start cmd /k "cd /d {self.jekyll_root} && {cmd}"', shell=True)
            else:
                subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 
                                f'cd "{self.jekyll_root}" && {cmd}; bash'])
            self.update_status(f"🔧 Running: jekyll {command}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to run command: {e}")
    
    def load_site(self):
        """Load Jekyll site on startup"""
        site_name = Path(self.jekyll_root).name
        self.update_status(f"📍 Loaded: {site_name}")
    
    def update_status(self, message):
        """Update status message"""
        self.status_var.set(message)
        self.root.after(3000, lambda: self.status_var.set("Ready"))  # Clear after 3s
    
    def run(self):
        """Start the application"""
        self.root.mainloop()

class ModernListDialog:
    """Modern list selection dialog"""
    def __init__(self, parent, title, items):
        self.result = None
        
        self.dialog = tk.Toplevel(parent)
        self.dialog.title(title)
        self.dialog.geometry("400x300")
        self.dialog.transient(parent)
        self.dialog.grab_set()
        
        # Center dialog
        self.dialog.update_idletasks()
        x = (self.dialog.winfo_screenwidth() // 2) - (200)
        y = (self.dialog.winfo_screenheight() // 2) - (150)
        self.dialog.geometry(f"400x300+{x}+{y}")
        
        # Modern styling
        self.dialog.configure(bg='#f8fafc')
        
        # Header
        header = tk.Frame(self.dialog, bg='#2563eb', height=50)
        header.pack(fill='x')
        header.pack_propagate(False)
        
        tk.Label(header, text=title, fg='white', bg='#2563eb', 
                font=('Segoe UI', 12, 'bold')).pack(expand=True)
        
        # Content
        content = tk.Frame(self.dialog, bg='#f8fafc')
        content.pack(fill='both', expand=True, padx=20, pady=20)
        
        # List
        self.listbox = tk.Listbox(content, font=('Segoe UI', 10),
                                 selectbackground='#2563eb', selectforeground='white',
                                 bg='white', relief='solid', bd=1)
        self.listbox.pack(fill='both', expand=True, pady=(0, 15))
        
        for item in items:
            self.listbox.insert(tk.END, item)
        
        if items:
            self.listbox.selection_set(0)
        
        # Buttons
        btn_frame = tk.Frame(content, bg='#f8fafc')
        btn_frame.pack(fill='x')
        
        tk.Button(btn_frame, text="Cancel", command=self.cancel,
                 bg='#e5e7eb', fg='#374151', relief='flat', padx=20, pady=8,
                 font=('Segoe UI', 10)).pack(side='right', padx=(10, 0))
        tk.Button(btn_frame, text="Select", command=self.ok,
                 bg='#2563eb', fg='white', relief='flat', padx=20, pady=8,
                 font=('Segoe UI', 10, 'bold')).pack(side='right')
        
        self.dialog.wait_window()
    
    def ok(self):
        selection = self.listbox.curselection()
        if selection:
            self.result = selection[0]
        self.dialog.destroy()
    
    def cancel(self):
        self.dialog.destroy()

if __name__ == "__main__":
    try:
        app = ModernJekyllGUI()
        app.run()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to start: {e}")
