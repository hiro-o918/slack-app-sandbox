from typing import Any
from slack_bolt import Ack
from logging import Logger

from slack_sdk import WebClient


def sample_command_callback(command: dict[str, Any], ack: Ack, logger: Logger, client: WebClient):
    try:
        ack()
        client.views_open(
            trigger_id=command["trigger_id"],
            view={
                "type": "modal",
                "callback_id": "move_to_next_view_id",
                "title": {"type": "plain_text", "text": "Sample modal title"},
                "blocks": [
                    {
                        "type": "input",
                        "block_id": "input_block_id",
                        "label": {
                            "type": "plain_text",
                            "text": "What are your hopes and dreams?",
                        },
                        "element": {
                            "type": "plain_text_input",
                            "action_id": "sample_input_id",
                            "multiline": True,
                        },
                    },
                    {
                        "block_id": "select_channel_block_id",
                        "type": "input",
                        "label": {
                            "type": "plain_text",
                            "text": "Select a channel to message the result to",
                        },
                        "element": {
                            "type": "conversations_select",
                            "action_id": "sample_dropdown_id",
                            "response_url_enabled": True,
                        },
                    },
                ],
                "submit": {"type": "plain_text", "text": "Submit"},
            },
        )

    except Exception as e:
        logger.error(e)
