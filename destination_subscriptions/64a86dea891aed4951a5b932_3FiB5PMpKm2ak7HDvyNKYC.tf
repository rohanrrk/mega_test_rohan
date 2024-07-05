import {
  to = segment_destination_subscription.id-64a86dea891aed4951a5b932_3FiB5PMpKm2ak7HDvyNKYC
  id = "64a86dea891aed4951a5b932:3FiB5PMpKm2ak7HDvyNKYC"
}

resource "segment_destination_subscription" "id-64a86dea891aed4951a5b932_3FiB5PMpKm2ak7HDvyNKYC" {
  action_id      = "i9V1H1emvbxxNuwB5bdALx"
  destination_id = "64a86dea891aed4951a5b932"
  enabled        = true
  model_id       = null
  name           = "Sync To LinkedIn DMP Segment"
  settings       = "{\"dmp_segment_name\":{\"@path\":\"$.properties.audience_key\"},\"email\":{\"@path\":\"$.context.traits.email\"},\"enable_batching\":true,\"event_name\":{\"@path\":\"$.event\"},\"google_advertising_id\":{\"@path\":\"$.context.device.advertisingId\"},\"personas_audience_key\":{\"@template\":\"mnmnmn{{context.active}}\"},\"source_segment_id\":{\"@path\":\"$.properties.audience_key\"}}"
  trigger        = "event = \"Audience Entered\" or event = \"Audience Exited\""
}