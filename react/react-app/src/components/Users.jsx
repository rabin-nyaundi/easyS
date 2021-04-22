import React, { Component } from 'react';
// import axios from 'react-axios'
import axios from 'axios';
import TableUsers from './TableUsers';
import Table from 'react-bootstrap/Table'



const api = axios.create({
    baseURL : `https://607e868602a23c0017e8b79e.mockapi.io/api/v1/users`
});


class Users extends Component {
    state = {
        users: [],
    }
    constructor() {
        super();
        this.getUsers();
    }

    getUsers = async() => {
        let data = await api.get('/').then(({ data }) => data);
            this.setState({users : data})
    }
    
    updateUser = async(id, val1) => {
        let data = await api.patch(`/${id}`, { name: val1 });
        this.setState({users:data})
        console.log(data);
        this.getUsers();
    }
    render() {
        console.log("The state", this.state);
        return (
            <div className="container">
                <h3>Table users</h3>
                {/* <TableUsers
                    onClick ={this.updateUser()}
                    users={this.state.users} /> */}
                <Table responsive="md" striped bordered hover size="sm">
                <thead>
                    <tr>
                        <th>Id</th>
                        <th>Name</th>
                        <th>Email</th>
                        <th>Username</th>
                        <th>Avatar</th>
                        <th>Phone Number</th>
                        <th>Created At</th>
                        <th>Action</th>
                    </tr>
                </thead>
                <tbody>
                    {this.state.users.map(user => (
                        <tr>
                            <td>{user.id}</td>
                            <td>{user.name}</td>
                            <td>{user.email}</td>
                            <td>{user.username}</td>
                            <td>{user.avatar}</td>
                            <td>{user.phoneNumber}</td>
                            <td>{user.createdAt}</td>
                            <td>
                                <button
                                    onClick={() => this.updateUser(user.id, `${user.name}a`)}
                                    className="btn btn-success"
                                >
                                    Edit
                                </button></td>
                        </tr>
                    ))}
                   
                </tbody>
            </Table>
            </div>

         );
    }
}

export default Users;