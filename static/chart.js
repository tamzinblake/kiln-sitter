'use strict'
$(function() {
  let chart = c3.generate({data: { columns: []}})
  let fetchData = () => {
    $.get('/temperature', (data) => {
      data = data.map((row) => {
        return row.temperature
      })
      data.unshift('temperatures')
      console.log(data)
      chart.load({columns: [data]})
    })
  }
  window.setInterval(fetchData, 10000)
  fetchData()
})
