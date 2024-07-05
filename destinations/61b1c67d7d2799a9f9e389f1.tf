import {
  to = segment_destination.id-61b1c67d7d2799a9f9e389f1
  id = "61b1c67d7d2799a9f9e389f1"
}

resource "segment_destination" "id-61b1c67d7d2799a9f9e389f1" {
  enabled = true
  metadata = {
    contacts          = null
    id                = "56748689e954a874ca44ccfb"
    partner_owned     = false
    region_endpoints  = ["US"]
    supported_regions = null
  }
  name      = "testslack1"
  settings  = "{\"channels\":[{\"channel\":\"#segemnt_channel\",\"eventName\":\"testevent\",\"regex\":false}],\"identifyTemplate\":\"\",\"templates\":[{\"eventName\":\"ewew\",\"regex\":false,\"template\":\"weeweweweqwew\"}],\"webhookUrl\":\"https://hooks.slack.com/services/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\",\"whiteListedTraits\":[]}"
  source_id = "3E3EYfjhbDqZroqeM1utvP"
}