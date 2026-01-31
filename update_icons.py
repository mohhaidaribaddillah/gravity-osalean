import os
import re

# Mapping Material Symbols to Bootstrap Icons
icon_mapping = {
    # CDN Link
    'href="https://fonts.googleapis.com/css2?family=Material+Symbols_Outlined:wght@100..700,0..1&display=swap"': 'href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css"',
    
    # Common Icons
    'material-symbols-outlined text-[20px]">notifications': 'bi bi-bell text-[20px]">',
    'material-symbols-outlined text-[20px]">settings': 'bi bi-gear text-[20px]">',
    'material-symbols-outlined text-[24px]">menu': 'bi bi-list text-[24px]">',
    'material-symbols-outlined">close': 'bi bi-x-lg">',
    'material-symbols-outlined">dashboard': 'bi bi-speedometer2">',
    'material-symbols-outlined">analytics': 'bi bi-graph-up">',
    'material-symbols-outlined">receipt_long': 'bi bi-receipt">',
    'material-symbols-outlined">inventory_2': 'bi bi-box-seam">',
    'material-symbols-outlined">article': 'bi bi-file-text">',
    'material-symbols-outlined text-lg">download': 'bi bi-download text-lg">',
    'material-symbols-outlined text-lg">filter_list': 'bi bi-funnel text-lg">',
    'material-symbols-outlined text-lg">payments': 'bi bi-credit-card text-lg">',
    'material-symbols-outlined text-sm">trending_up': 'bi bi-graph-up-arrow text-sm">',
    'material-symbols-outlined text-lg">shopping_cart': 'bi bi-cart text-lg">',
    'material-symbols-outlined text-sm">trending_down': 'bi bi-graph-down-arrow text-sm">',
    'material-symbols-outlined text-[140px] text-primary">public': 'bi bi-globe text-[140px] text-primary">',
    'material-symbols-outlined">location_on': 'bi bi-geo-alt-fill">',
    'material-symbols-outlined text-2xl">arrow_upward': 'bi bi-arrow-up text-2xl">',
    'material-symbols-outlined">attach_money': 'bi bi-currency-dollar">',
    'material-symbols-outlined">conversion_path': 'bi bi-shuffle">',
    'material-symbols-outlined">shopping_bag': 'bi bi-bag">',
    'material-symbols-outlined">groups': 'bi bi-people">',
    'material-symbols-outlined">search': 'bi bi-search">',
    'material-symbols-outlined">link': 'bi bi-link-45deg">',
    'material-symbols-outlined">share': 'bi bi-share">',
    'material-symbols-outlined">email': 'bi bi-envelope">',
    'material-symbols-outlined text-2xl text-primary">schedule': 'bi bi-clock text-2xl text-primary">',
    'material-symbols-outlined text-2xl text-blue-500">pageview': 'bi bi-file-earmark-text text-2xl text-blue-500">',
    'material-symbols-outlined text-2xl text-purple-500">exit_to_app': 'bi bi-box-arrow-right text-2xl text-purple-500">',
    'material-symbols-outlined text-2xl text-orange-500">replay': 'bi bi-arrow-repeat text-2xl text-orange-500">',
    'material-symbols-outlined text-lg">visibility': 'bi bi-eye text-lg">',
    'material-symbols-outlined text-lg">send': 'bi bi-send text-lg">',
    'material-symbols-outlined text-sm">check_circle': 'bi bi-check-circle text-sm">',
    'material-symbols-outlined text-sm">schedule': 'bi bi-clock text-sm">',
    'material-symbols-outlined text-sm">error': 'bi bi-exclamation-circle text-sm">',
    'material-symbols-outlined text-lg">add': 'bi bi-plus-lg text-lg">',
    'material-symbols-outlined text-lg">favorite_border': 'bi bi-heart text-lg">',
    'material-symbols-outlined text-sm">star': 'bi bi-star-fill text-sm">',
    'material-symbols-outlined">expand_more': 'bi bi-chevron-down">',
}

# Files to process
files = [
    'analytics.html',
    'invoice.html',
    'products.html',
    'blog.html'
]

base_path = r'c:\antygrafity\osalean-dashboard'

for filename in files:
    filepath = os.path.join(base_path, filename)
    
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        continue
    
    # Read file
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace all occurrences
    for old, new in icon_mapping.items():
        content = content.replace(old, new)
    
    # Replace any remaining material-symbols-outlined with bi
    content = re.sub(r'<span class="material-symbols-outlined([^"]*)">', r'<i class="bi\1">', content)
    content = re.sub(r'</span>', '</i>', content)
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Updated {filename}")

print("\n✅ All files updated successfully!")
