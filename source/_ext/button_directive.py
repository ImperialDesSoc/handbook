# Custom extension for the button directive.
# 
# Ben Greenberg (github.com/nebbles)
# 10 July 2019
#
# This work is based on https://github.com/conda/conda-docs/blob/04613488d57688d77b0bc20618b9a4d5b56947ed/web/button.py
# Referenced from this SO post https://stackoverflow.com/questions/25088113/make-a-css-button-a-link-in-sphinx
#

from __future__ import absolute_import
from docutils import nodes
import jinja2
from docutils.parsers.rst.directives import unchanged
from docutils.parsers.rst import Directive

BUTTON_TEMPLATE = jinja2.Template(u"""
<div style="text-align:center">
  <a href="{{ link }}">
  <span class="btn btn-info btn-custom" >{{ text }}</span>
  </a>
</div>
""")


class button_node(nodes.General, nodes.Element):
    pass


# This directive will be used when generating the node graph on first pass
# of the source files. When the node is visited, the run() method is run.
class ButtonDirective(Directive):
    required_arguments = 0

    option_spec = {
        'text': unchanged,
        'link': unchanged,
    }

    def run(self):
        env = self.state.document.settings.env
        app = env.app

        app.add_stylesheet('button.css')

        node = button_node()
        node['text'] = self.options['text']
        node['link'] = self.options['link']
        return [node]

# This function converts node date into actual HTML using the jinja template
# defined above.
def html_visit_button_node(self, node):
    html = BUTTON_TEMPLATE.render(text=node['text'], link=node['link'])
    self.body.append(html)
    raise nodes.SkipNode


def latex_visit_button_node(self, node):
    # html = BUTTON_TEMPLATE.render(text=node['text'], link=node['link'])
    # self.body.append(html)
    raise nodes.SkipNode

# More visit function can be defined for latex, text, etc. outputs too
# Other visit functions should be added as add_node() kwargs. 
def setup(app):
    app.add_node(button_node,
                 html=(html_visit_button_node, None),
                 latex=(latex_visit_button_node, None))
    app.add_directive('button', ButtonDirective)
