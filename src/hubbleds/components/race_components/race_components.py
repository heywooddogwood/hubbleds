import ipyvuetify as v
from cosmicds.utils import load_template
from glue_jupyter.state_traitlets_helpers import GlueState
from traitlets import Float, Bool, Int, Unicode, List


class Race(v.VuetifyTemplate):
    template = Unicode().tag(sync=True)
    state = GlueState().tag(sync=True)
    story_state = GlueState().tag(sync=True)

    def __init__(self, filename, path, state, story_state, *args, **kwargs):
        self.state = state
        self.story_state = story_state
        super().__init__(*args, **kwargs)
        self.template = load_template(filename, path)
