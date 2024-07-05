import {
  to = segment_destination_subscription.id-63f8eb614d63af9d5449a7c7_bxntiwrB25qYwLpg3Motuu
  id = "63f8eb614d63af9d5449a7c7:bxntiwrB25qYwLpg3Motuu"
}

resource "segment_destination_subscription" "id-63f8eb614d63af9d5449a7c7_bxntiwrB25qYwLpg3Motuu" {
  action_id      = "6cgExzDArNQSaKL9TwFHTP"
  destination_id = "63f8eb614d63af9d5449a7c7"
  enabled        = false
  model_id       = "upfQTKtX98eXoEoDcWcagv"
  name           = "Post Sheet"
  settings       = "{\"data_format\":\"RAW\",\"enable_batching\":false,\"fields\":{\"Test\":\"Data\",\"Test1\":\"Data\"},\"operation_type\":{\"@path\":\"$.event\"},\"record_identifier\":{\"@path\":\"$.properties.user_id\"},\"spreadsheet_id\":\"1SUgE9nE2DJ4hm3z9-ZjJ6PpDGy86qFPO6O5s8J9TE1k\",\"spreadsheet_name\":\"Sheet1\"}"
  trigger        = "event = \"new\""
}