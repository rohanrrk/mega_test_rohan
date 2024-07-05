import {
  to = segment_user_group.id-2TAEzIwXorLu02NClDmsW0RQfWX
  id = "2TAEzIwXorLu02NClDmsW0RQfWX"
}

resource "segment_user_group" "id-2TAEzIwXorLu02NClDmsW0RQfWX" {
  members = ["admin+4@rohanevildoer.in"]
  name    = "newspace"
  permissions = [
    {
      resources = [
        {
          id = "r6UY6oUJ67jL4qSWjxLM5D"
          labels = [
          ]
          type = "WORKSPACE"
        },
      ]
      role_id = "1Mc8DFMmZbyzdEWmE6k8JVgKAiE"
    },
  ]
}