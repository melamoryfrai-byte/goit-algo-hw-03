import matplotlib.pyplot as plt
import numpy as np

def koch_segment(p1, p2, order):
    """Generate Koch curve segment between two points"""
    if order == 0:
        return [p1, p2]
    
    # Divide line into three parts
    dx = (p2[0] - p1[0]) / 3
    dy = (p2[1] - p1[1]) / 3

    # Calculate five points
    a = p1
    b = (p1[0] + dx, p1[1] + dy)
    # IMPORTANT: Use NEGATIVE angle (-np.pi/3) to point outward
    c = (b[0] + dx * np.cos(-np.pi/3) - dy * np.sin(-np.pi/3),
         b[1] + dx * np.sin(-np.pi/3) + dy * np.cos(-np.pi/3))
    d = (p1[0] + 2*dx, p1[1] + 2*dy)
    e = p2
    
    # Recursively apply to each segment
    points = []
    points.extend(koch_segment(a, b, order - 1)[:-1])
    points.extend(koch_segment(b, c, order - 1)[:-1])
    points.extend(koch_segment(c, d, order - 1)[:-1])
    points.extend(koch_segment(d, e, order - 1))
    
    return points

def koch_snowflake(order, size=300):
    """Generate Koch snowflake from equilateral triangle (pointing upward)"""
    # Calculate triangle vertices (triangle pointing UP)
    h = size * np.sqrt(3) / 2  # Height of equilateral triangle
    vertices = [
        (0, h * 2/3),        # Top vertex (pointing up)
        (-size/2, -h/3),     # Bottom left
        (size/2, -h/3)       # Bottom right
    ]
    
    # Generate Koch curve for each side of triangle
    all_points = []
    for i in range(3):
        side = koch_segment(vertices[i], vertices[(i+1) % 3], order)
        all_points.extend(side[:-1])  # Avoid duplicating vertices
    
    # Close the shape
    all_points.append(all_points[0])
    
    # Extract x and y coordinates
    x = [p[0] for p in all_points]
    y = [p[1] for p in all_points]
    
    return x, y

def draw_koch_snowflake(order, size=300):
    """Draw Koch snowflake"""
    x, y = koch_snowflake(order, size)
    
    plt.figure(figsize=(10, 10))
    plt.plot(x, y, 'b-', linewidth=2)
    plt.fill(x, y, alpha=0.3, color='lightblue')
    plt.title(f'Сніжинка Коха (порядок {order})', fontsize=14, fontweight='bold')
    plt.axis('equal')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

def compare_snowflake_orders():
    """Compare different orders side by side"""
    fig, axes = plt.subplots(2, 2, figsize=(14, 14))
    orders = [0, 1, 2, 3]
    
    for idx, order in enumerate(orders):
        ax = axes[idx // 2, idx % 2]
        x, y = koch_snowflake(order, size=200)
        ax.plot(x, y, 'b-', linewidth=2)
        ax.fill(x, y, alpha=0.3, color='lightblue')
        ax.set_title(f'Порядок {order}', fontsize=12, fontweight='bold')
        ax.axis('equal')
        ax.grid(True, alpha=0.3)
    
    plt.suptitle('Еволюція сніжинки Коха', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.show()


# Виклик функцій
draw_koch_snowflake(0)   # Triangle (starting point)
draw_koch_snowflake(1)   # First iteration (Star of David)
draw_koch_snowflake(2)   # Second iteration
draw_koch_snowflake(3)   # Third iteration (smooth snowflake)
draw_koch_snowflake(4)   # Fourth iteration (very smooth)

# Compare all orders at once
compare_snowflake_orders()