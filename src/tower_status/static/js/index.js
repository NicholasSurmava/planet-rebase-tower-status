(() => {
  var dropdown = document.querySelector(".dropdown");
  dropdown.addEventListener("click", function (event) {
    event.stopPropagation();
    dropdown.classList.toggle("is-active");
  });

  let site_id = document.querySelector('[data-js="site_id"]');
  let tickets_url = "/site_report/__tickets";
  let ticket_table = document.querySelector('[data-js="ticket_table"]');

  let fetch_tickets = () => {
    data = { site_id: site_id.textContent };
    // console.log(site_id.textContent);

    let loader = `<progress class="progress is-small is-primary" max="100">15%</progress>`;
    ticket_table.innerHTML = loader;

    fetch(tickets_url, {
      method: "POST", // or 'PUT'
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("Success:", data);
        console.log(typeof data);
        if (data === null) {
          ticket_table.textContent = "No Tickets";
        } else {
          ticket_table.textContent = data.summary + data.id;
        }

        console.log(ticket_table);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  };

  let get_tickets_btn = document.querySelector('[data-js="get_tickets_btn"]');
  // console.log(get_tickets_btn);

  get_tickets_btn.addEventListener("click", fetch_tickets);

  fetch_tickets();
})();
