from pathlib import Path
def generate_bar_chart(data, width=600, height=400, bar_width=40, bar_spacing=10):
    svg = '<svg xmlns="http://www.w3.org/2000/svg" width="{0}" height="{1}">'.format(width, height)

    max_value = max(data)
    bar_height_ratio = (height - bar_spacing) / max_value

    x = bar_spacing
    for index, value in enumerate(data):
        bar_height = value * bar_height_ratio
        bar_y = height - bar_height

        # Create the bar
        rect_svg = '<rect x="{0}" y="{1}" width="{2}" height="{3}" fill="steelblue" class="bar">'.format(x, bar_y, bar_width, bar_height)

        # Add value as extra information
        rect_svg += '<title>Value: {0}</title>'.format(value)

        # Close the bar element
        rect_svg += '</rect>'

        # Add a text element for hover display
        text_x = x + bar_width / 2
        text_y = bar_y - 5
        text_svg = '<text x="{0}" y="{1}" text-anchor="middle" class="hover-text" visibility="hidden">{2}</text>'.format(
            text_x, text_y, value)

        svg += rect_svg + text_svg
        x += bar_width + bar_spacing

    svg += '</svg>'

    # Add CSS styles for hover effect and fading
    svg += '''
        <style>
            .bar:hover {
                fill: orange;
                opacity: 1;
            }
            .bar {
                transition: opacity 0.3s;
                opacity: 0.5;
            }
            .hover-text {
                visibility: hidden;
            }
            .bar:hover + .hover-text {
                visibility: visible;
            }
        </style>
    '''

    return svg


# Example data
items = [5, 8, 12, 6, 10]

# Generate SVG bar chart
chart_svg = generate_bar_chart(items)

# Print the SVG code
print(chart_svg)




Path("test2.html").write_text(chart_svg)