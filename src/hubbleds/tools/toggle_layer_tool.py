from bqplot.marks import Label, Lines
from echo import add_callback, CallbackProperty
from glue.config import viewer_tool
from glue.viewers.common.tool import CheckableTool, Tool

from ..utils import H_ALPHA_REST_LAMBDA, MG_REST_LAMBDA


@viewer_tool
class LayerToggleTool(Tool):
    tool_id = "hubble:togglelayer"
    action_text = "Toggle display of the classes data"
    tool_tip = "Toggle display of the classes data"
    mdi_icon = "mdi-google-classroom"

    base_layer = 'mine'
    class_layer = 'class'

    def __init__(self, viewer, **kwargs):
        super().__init__(viewer, **kwargs)
        self.layer_index = 0
    

    def activate(self):
        # if we have no layers, don't do anything
        if len(self.viewer.layers) > 0:
            self.layer_to_toggle.visible = not self.layer_to_toggle.visible
    
    def set_layer_to_toggle(self, layer = None):
        if layer is not None:
            self.layer_to_toggle = layer
        else:
            self.layer_to_toggle = self.viewer.layers[self.layer_index]
        
    def _on_view_change(self, event=None):
        pass