import {
  to = segment_destination_subscription.id-63f8eb614d63af9d5449a7c7_jZHHn34DfAf1v8cgvRPu4v
  id = "63f8eb614d63af9d5449a7c7:jZHHn34DfAf1v8cgvRPu4v"
}

resource "segment_destination_subscription" "id-63f8eb614d63af9d5449a7c7_jZHHn34DfAf1v8cgvRPu4v" {
  action_id      = "6cgExzDArNQSaKL9TwFHTP"
  destination_id = "63f8eb614d63af9d5449a7c7"
  enabled        = false
  model_id       = "upfQTKtX98eXoEoDcWcagv"
  name           = "Post Sheet"
  settings       = "{\"operation_type\":{\"@path\":\"$.event\"}}"
  trigger        = "event = \"updated\" or event = \"new\""
}