function deleteProject(pro_id, csrf_token) {
    const data = {pro_id: pro_id}
    // กำหนด path ให้ถูกต้อง
    fetch(`/employee/project/`, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrf_token,
      },
      body: JSON.stringify(data),
    })
      .then((data) => {
        console.log("Item deleted successfully");
        window.location.reload();
      })
      .catch((error) => console.error("Error:", error));
  }
