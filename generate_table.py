import json

with open("data.json","rb") as f:
    data = json.load(f)
    with open("temp-table.html", "w") as t:
        for item in data.get("resources"):
            tr = f'''
            <tr>
                <th scope="row">
                  <a
                    href="{item.get("link")}"
                    >{item.get("charity_name")}</a
                  >
                </th>
                <td>{item.get("regional")}</td>
                <td>{item.get("mission")}</td>
                <td>{item.get("accepting_non_inr")}</td>
              </tr>
            '''
            t.write(tr + "\n")
