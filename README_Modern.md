# Jekyll Compose - Modern Edition 🎯

A sleek, modern GUI application for Jekyll content creation with a simplified, clean codebase and contemporary design.

![Modern UI](https://img.shields.io/badge/UI-Modern-blue) ![Code](https://img.shields.io/badge/Code-Simplified-green) ![Python](https://img.shields.io/badge/Python-3.6+-blue)

## ✨ Features

### 🎨 **Ultra-Modern Design**
- **Clean Interface**: Minimalist design with modern color scheme
- **Responsive Layout**: Sidebar navigation with main content area
- **Visual Feedback**: Status indicators, hover effects, and smooth interactions
- **Professional Typography**: Segoe UI font with proper spacing and hierarchy

### ⚡ **Simplified Workflow**
- **Quick Actions**: One-click access to common tasks
- **Smart Forms**: Context-aware form dialogs with validation
- **File Browser**: Built-in recent files list with double-click to open
- **Live Status**: Real-time feedback with auto-clearing status messages

### 🔧 **Core Functionality**
- ✅ Create posts, drafts, pages, and collection files
- ✅ Publish/unpublish with one click
- ✅ Auto-open files in default editor
- ✅ Jekyll build and serve integration
- ✅ Smart file naming and front matter generation

## 🚀 Quick Start

### Option 1: Run with Launcher (Recommended)
```cmd
# Double-click this file or run in terminal
run_modern_gui.bat
```

### Option 2: Manual Start
```cmd
# Install dependencies (one-time)
pip install pyyaml

# Run the application
python jekyll_compose_modern.py
```

## 🎯 Interface Overview

### **Header Section**
- **Title & Subtitle**: App branding and description
- **Quick Actions**: Build, Serve, and Open Folder buttons

### **Sidebar Navigation**
- **Jekyll Site**: Current site path with change option
- **Quick Actions**: Icon-labeled buttons for common tasks
- **Recent Files**: List of recently modified files

### **Main Content Area**
- **Welcome Screen**: Getting started guide and quick actions
- **Form Views**: Modern form dialogs for content creation
- **Live Preview**: Real-time feedback and status

### **Footer Status Bar**
- **Status Indicator**: Green dot with current operation status
- **Settings**: Auto-open files toggle

## 📝 Content Creation

### **Posts** ✏️
1. Click "New Post" in sidebar or welcome screen
2. Fill in title, date (optional), and format
3. Click "Create" - file opens automatically if enabled

### **Drafts** 📝
1. Click "New Draft"
2. Enter title
3. File created in `_drafts/` folder

### **Pages** 📄
1. Click "New Page"
2. Enter title
3. File created in `_pages/` folder

### **Collection Files** 📚
1. Click "Collection File"
2. Enter title and select collection
3. File created in appropriate `_{collection}/` folder

## ⚡ Quick Operations

### **Publishing Workflow**
1. **Publish Draft**: Select from list → Auto-dated and moved to `_posts/`
2. **Unpublish Post**: Select from list → Date removed and moved to `_drafts/`

### **Site Management**
- **Build Site**: Runs `bundle exec jekyll build` in new terminal
- **Serve Site**: Runs `bundle exec jekyll serve` in new terminal
- **Open Folder**: Opens Jekyll root in file explorer

## 🎨 Design Philosophy

### **Modern Visual Design**
```
Color Scheme:
- Primary: #2563eb (Blue)
- Secondary: #64748b (Slate)  
- Success: #10b981 (Green)
- Background: #f8fafc (Light Gray)
- Cards: #ffffff (White)
```

### **Simplified Code Architecture**
- **Single Class Design**: `ModernJekyllGUI` handles all functionality
- **Method Organization**: Logical grouping by feature area
- **Minimal Dependencies**: Only PyYAML for config parsing
- **Clean Separation**: UI, logic, and file operations clearly separated

## 🔧 Technical Details

### **File Structure**
```
jekyll_compose_modern.py     # Main application (< 500 lines)
run_modern_gui.bat          # Windows launcher
README_Modern.md            # This documentation
.jekyll_gui_config.json     # User settings (auto-created)
```

### **Key Improvements Over Previous Versions**
1. **50% Less Code**: Simplified from 1200+ to ~500 lines
2. **Modern UI**: Contemporary design with professional styling
3. **Better UX**: Intuitive navigation and visual feedback
4. **Cleaner Architecture**: Single-file solution with clear organization
5. **Faster Performance**: Reduced complexity and better resource usage

### **Configuration**
Settings are automatically saved to `.jekyll_gui_config.json`:
```json
{
  "auto_open": true
}
```

## 🔄 Comparison with CLI

| Action | CLI Command | Modern GUI |
|--------|-------------|------------|
| New Post | `bundle exec jekyll post "Title"` | Click "New Post" → Fill form |
| New Draft | `bundle exec jekyll draft "Title"` | Click "New Draft" → Enter title |
| Publish | `bundle exec jekyll publish _drafts/file.md` | Click "Publish Draft" → Select from list |
| Build | `bundle exec jekyll build` | Click "Build" button |
| Serve | `bundle exec jekyll serve` | Click "Serve Site" button |

## 🎯 Workflow Examples

### **Creating Your First Post**
1. Start the app → Modern welcome screen appears
2. Click "📝 Create Post" → Form opens
3. Enter "My Awesome Post" → Click "Create"
4. File opens in your default editor automatically
5. Status shows "✓ Post created: 2025-07-12-my-awesome-post.md"

### **Managing Drafts**
1. Create draft → Click "📝 New Draft"
2. Write content in your editor
3. Ready to publish? → Click "🚀 Publish Draft"
4. Select from list → Automatically dated and published
5. Status shows "🚀 Published: 2025-07-12-my-draft.md"

## 🚀 Advanced Features

### **Smart File Naming**
- Automatic slug generation from titles
- Date prefixing for posts
- Collision detection with overwrite prompts

### **Front Matter Generation**
```yaml
---
title: Your Title Here
date: 2025-07-12  # Auto-added for posts
---
```

### **Collection Auto-Detection**
- Scans for `_{name}` folders
- Includes standard collections (posts, drafts, pages)
- Dynamic dropdown population

## 🔧 Troubleshooting

### **Common Issues**

1. **"Jekyll root not found"**
   - Ensure you're in a Jekyll site directory
   - Look for `_config.yml` file
   - Use "Change Location" to manually select

2. **"Auto-open not working"**
   - Check your default `.md` file association
   - Try manually opening a created file
   - Toggle the setting in footer

3. **"Command failed"**
   - Ensure Jekyll and Bundler are installed
   - Check if you're in the correct directory
   - Verify `Gemfile` exists

### **Performance Tips**
- Keep recent files list under 20 items (automatic)
- Close unused forms by clicking "Cancel"
- Use quick actions for frequent operations

## 🎉 What's New in Modern Edition

### **Visual Improvements**
- ✨ Contemporary design with professional color scheme
- 🎯 Icon-enhanced navigation for better usability
- 💡 Smart status system with auto-clearing messages
- 🖼️ Card-based layout with proper spacing

### **Code Improvements**
- 📦 Single-file architecture (no external dialog classes)
- ⚡ 60% reduction in code complexity
- 🔧 JSON-based configuration (simpler than YAML)
- 🏗️ Modular method organization

### **UX Improvements**
- 🚀 One-click publish/unpublish workflows
- 📋 Recent files browser with double-click open
- ⚙️ Persistent settings with auto-save
- 🎨 Modern form dialogs with proper validation

## 📄 License

Same as Jekyll Compose - MIT License

---

**Happy blogging with Jekyll Compose Modern! 🎉**
