function addStaff(project_id, csrf_token){
  const emp = document.getElementById('input-add-staff');
  const data = {emp_id: emp.value};

  // กำหนด path ให้ถูกต้อง
  fetch(`/employee/project/${project_id}/`, {
      method: 'PUT',
      headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrf_token,
      },
      body: JSON.stringify(data)
  })
  .then(response => response.json())
  .then(data => {
      console.log('Item updated successfully')
      window.location.reload()
  })
  .catch(error => console.error('Error:', error));
}

function removeStaff(pro_id, emp_id, csrf_token) {
    const data = { emp_id: emp_id }
    // กำหนด path ให้ถูกต้อง
    fetch(`/employee/project/${pro_id}/`, {
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
