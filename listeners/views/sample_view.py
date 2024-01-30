from logging import Logger

from slack_bolt import Ack
from slack_sdk import WebClient


def sample_view_callback(view, ack: Ack, body: dict, client: WebClient, logger: Logger):
    try:
        ack()
        sample_user_value = body["user"]["id"]
        provided_values = view["state"]["values"]
        logger.info(f"Provided values {provided_values}")
        sample_input_value = provided_values["input_block_id"]["sample_input_id"]["value"]
        sample_convo_value = provided_values["select_channel_block_id"]["sample_dropdown_id"]["selected_conversation"]

        client.chat_postMessage(
            channel=sample_convo_value,
            blocks=[
                {"type": "section", "text": {"type": "mrkdwn", "text": "Hi"}},
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"""*Channel:*: <#{sample_convo_value}>
*Answer:* {sample_input_value}
*Asked by:* <@{sample_user_value}>
""",
                    },
                    "accessory": {
                        "type": "image",
                        "image_url": "https://api.slack.com/img/blocks/bkb_template_images/approvalsNewDevice.png",
                        "alt_text": "computer thumbnail",
                    },
                },
                {
                    "type": "divider",
                },
                {
                    "type": "actions",
                    "elements": [
                        {
                            "type": "button",
                            "text": {"type": "plain_text", "emoji": True, "text": "Solved"},
                            "style": "primary",
                            "value": "click_me_123",
                            "action_id": "solved_action_id",
                        },
                        {
                            "type": "button",
                            "text": {"type": "plain_text", "emoji": True, "text": "Pending"},
                            "style": "danger",
                            "value": "click_me_123",
                            "action_id": "pending_action_id",
                        },
                    ],
                },
            ],
        )
    except Exception as e:
        logger.error(e)


def move_to_next_view_callback(view: dict, ack: Ack, body: dict, client: WebClient, logger: Logger):
    try:
        ack()
        provided_values = view["state"]["values"]

        default_input_value = "前回の入力：" + provided_values["input_block_id"]["sample_input_id"]["value"]
        default_sample_convo_value = provided_values["select_channel_block_id"]["sample_dropdown_id"][
            "selected_conversation"
        ]

        client.views_open(
            trigger_id=body["trigger_id"],
            view={
                "type": "modal",
                "callback_id": "sample_view_id",
                "title": {
                    "type": "plain_text",
                    "text": "Move to next",
                },
                "blocks": [
                    {
                        "type": "input",
                        "block_id": "input_block_id",
                        "label": {
                            "type": "plain_text",
                            "text": "We can receive the previous input value",
                        },
                        "element": {
                            "type": "plain_text_input",
                            "action_id": "sample_input_id",
                            "initial_value": default_input_value,
                            "multiline": True,
                        },
                    },
                    {
                        "block_id": "select_channel_block_id",
                        "type": "input",
                        "label": {
                            "type": "plain_text",
                            "text": "Also the previous conversation selection value",
                        },
                        "element": {
                            "type": "conversations_select",
                            "action_id": "sample_dropdown_id",
                            "initial_conversation": default_sample_convo_value,
                            "response_url_enabled": True,
                        },
                    },
                ],
                "submit": {"type": "plain_text", "text": "Submit"},
            },
        )
    except Exception as e:
        logger.error(e)
