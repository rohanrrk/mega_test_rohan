import {
  to = segment_source.id-fLyCdqjyhvxhdCJyNEvZFF
  id = "fLyCdqjyhvxhdCJyNEvZFF"
}

resource "segment_source" "id-fLyCdqjyhvxhdCJyNEvZFF" {
  enabled = true
  labels = [
    {
      key   = "environment"
      value = "dev"
    },
  ]
  metadata = {
    id = "iUM16Md8P2"
  }
  name     = "HTTP API"
  settings = "{}"
  slug     = "http_api"
}