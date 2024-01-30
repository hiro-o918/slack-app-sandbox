from slack_bolt import App
from .sample_action import sample_action_callback, move_to_next_action_callback, solved_action, pended_action


def register(app: App):
    app.action("sample_action_id")(sample_action_callback)
    app.action("move_to_next_action_id")(move_to_next_action_callback)
    app.action("solved_action_id")(solved_action)
    app.action("pending_action_id")(pended_action)
