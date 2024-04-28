document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        events: '/api/events',
        eventColor: '#378006',
        eventContent: function(arg) {
            let container = document.createElement('div');
            container.classList.add('event-container');

            let emojiSpan = document.createElement('span');
            emojiSpan.classList.add('emoji');
            
            if(arg.event.title.includes('POSITIVE')) {
                emojiSpan.innerText = '😄'; 
            } else if(arg.event.title.includes('NEGATIVE')) {
                emojiSpan.innerText = '😔'; 
            } else {
                emojiSpan.innerText = '😐'; 
            }
            
            let scoreSpan = document.createElement('span');
            scoreSpan.classList.add('score');
            scoreSpan.innerText = arg.event.title.split('-')[1].trim(); 
            
            container.appendChild(emojiSpan);
            container.appendChild(scoreSpan);

            return { domNodes: [container] };
        },
        eventClick: function(arg) {
            
            showEventDetails(arg.event);
        }
    });
    calendar.render();
});

function showEventDetails(event) {
    let detailBox = document.getElementById('event-detail-box');
    let title = detailBox.querySelector('.title');
    let score = detailBox.querySelector('.score');

    title.innerText = event.title.split('-')[0];
    score.innerText = 'Score: ' + event.title.split('-')[1].trim();

    detailBox.style.opacity = 0;
    detailBox.style.display = 'block';
    setTimeout(function() {
        detailBox.style.opacity = 1;
    }, 10);
}

document.getElementById('close-detail-box').addEventListener('click', function() {
    document.getElementById('event-detail-box').style.display = 'none';
});

